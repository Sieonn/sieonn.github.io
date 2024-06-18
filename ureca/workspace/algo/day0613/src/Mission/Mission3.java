package Mission;

import java.util.Arrays;

public class Mission3 {
	public static void main(String[] args) {
		Person p = new Person("갓길동",11,"학생",95);
		Person[] persons= {p ,
		        new Person("빛길동",19,"학생",80),
			      new Person("남길동",14,"학생",100),
			      new Person("여길동",17,"학생",99),
			      new Person("킹길동",15,"학생",56)};
		Arrays.sort(persons);
//		for (Person person : persons) {
//		    System.out.printf("Name: %s, Age: %d, Job: %s, Year: %d\n", person.name, person.age, person.job, person.year);
//		}
		
		
//		for (Person person : persons) {
//		    System.out.println("Name: " + person.name + ", Age: " + person.age + ", Job: " + person.job + ", Year: " + person.year);
//		}

		for (Person person : persons) {
		    System.out.println(person);
		}

	}
}
