package basico3;

public class exercicio7 {
	public static void main(String[] args) {
		String texto[] = {"a", "vida","é","bela"};
		String texto2 = " ";
		
		for (int x = texto.length -1; x >=0; x-- ) {
			texto2+= texto[x] +" ";
		}
		System.out.println(texto2.toUpperCase());
	}
}
