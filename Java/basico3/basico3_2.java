package basico3;

public class basico3_2 {

	public static void main(String[] args) {
		String str = "Hello";
		String resultado = str.toUpperCase();
		System.out.println(resultado);
		
		String str2 = " Hello ";
		String resultado2 = str.trim();
		System.out.println(resultado2);
		
		String s1 = "Hello";
		String s2 = "HELLO";
		
		boolean b1 = s1.equals("Hello");
		boolean b2 = s1.equals(s2);
		boolean b3 = s1.equalsIgnoreCase(s2);
		boolean b4 = s1.equalsIgnoreCase("azul");
		
		System.out.println(b1);
		System.out.println(b2);
		System.out.println(b3);
		System.out.println(b4);
	}
}
