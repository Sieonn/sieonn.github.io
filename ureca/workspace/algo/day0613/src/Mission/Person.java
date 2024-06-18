package Mission;

public class Person implements Comparable<Person> {
    String name;
    int age;
    String job;
    int year;
    
    public Person(String name, int age, String job, int year) {
        this.name = name;
        this.age = age;
        this.job = job;
        this.year = year;
    }
    
    //=> Person이름을 오름차순 정렬하시오.
    @Override
    public int compareTo(Person other) {
        return this.name.compareTo(other.name);
    }
    
	@Override
	public String toString() {
		return "[name:" + name + " age:" + age + " job:" + job + " year:" + year + "]";
	}
    
    
}
