class Foo {
	public void storePerson(Person input) throws IOException {
		try{
		//Dangerous Operation
		} catch (AnyException ae) {
		} 
		finally {
			try {
			//close connection but it may fail too
			} catch (IOException ioe) {
			//Log that
			}
		}
    }
}