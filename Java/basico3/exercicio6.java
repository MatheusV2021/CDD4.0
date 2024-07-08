package basico3;

public class exercicio6 {
	public static void main(String[] args) {
		String texto[] = {"a", "vida","é","bela"};
		String texto2 = " ";
		
		for (String x : texto) {
			texto2+= x+" ";
		}
		System.out.println(texto2.toUpperCase());
	}
}
