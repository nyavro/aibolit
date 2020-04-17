from javalang.tree import IfStatement, SwitchStatement, ForStatement, WhileStatement
from javalang.tree import DoStatement, CatchClause, BreakStatement, ContinueStatement
from javalang.tree import TernaryExpression, BinaryOperation, MethodDeclaration, MethodInvocation
from aibolit.utils.ast import AST
import javalang
from typing import List, Any, Type

increment_for: List[Type] = [
    IfStatement,
    SwitchStatement,
    ForStatement,
    WhileStatement,
    DoStatement,
    CatchClause,
    BreakStatement,
    ContinueStatement,
    TernaryExpression,
    BinaryOperation,
    MethodInvocation,
]

nested_for: List[Type] = [
    IfStatement,
    SwitchStatement,
    ForStatement,
    WhileStatement,
    DoStatement,
    CatchClause,
]

logical_operators: List[str] = ['&', '&&', '^', '|', '||']


class CognitiveComplexity:
    '''
    beta version of Cognitive Complexity
    '''
    def __init__(self):
        self.complexity = 0
        self.method_name = None

    def traverse_childs(self, block: Any, nested_level: int) -> None:

        for each_child in block.children:
            self.get_complexity(each_child, nested_level)

    def increment_logical_operators(self, block: BinaryOperation, prev_operator: str) -> None:
        for each_block in [block.operandr, block.operandl]:

            if isinstance(each_block, BinaryOperation) and prev_operator in logical_operators:
                if prev_operator != each_block.operator:
                    self.complexity += 1

                elif isinstance(each_block.operandr, BinaryOperation):
                    self.complexity += 1

                self.increment_logical_operators(each_block, each_block.operator)

    def is_recursion_call(self, block: MethodInvocation) -> bool:
        if self.method_name == block.member:
            return True
        return False

    def get_complexity(self, block: Any, nested_level: int) -> None:
        block_arr = block if isinstance(block, List) else [block]

        for each_block in block_arr:
            if hasattr(each_block, 'children'):
                if type(each_block) in increment_for and type(each_block) in nested_for:
                    self.complexity += 1 + nested_level
                    self.traverse_childs(each_block, nested_level + 1)

                elif type(each_block) in increment_for and type(each_block) not in nested_for:
                    if isinstance(each_block, BinaryOperation):
                        if each_block.operator in logical_operators:
                            self.complexity += 1
                            self.increment_logical_operators(each_block, each_block.operator)

                    elif isinstance(each_block, MethodInvocation):
                        is_recursion = self.is_recursion_call(each_block)
                        self.complexity += is_recursion

                    else:
                        self.complexity += 1
                        self.traverse_childs(each_block, nested_level)

                else:
                    self.traverse_childs(each_block, nested_level)

    def value(self, filename: str) -> int:

        tree = AST(filename).value()
        for _, class_body in tree.filter(javalang.tree.ClassDeclaration):
            for method in (class_body.body):
                if isinstance(method, MethodDeclaration):

                    # memorize the name for detecting recursion call
                    self.method_name = method.name
                    self.get_complexity(method, 0)

        final_value, self.complexity = self.complexity, 0
        return final_value
