package basico3;

import java.util.Scanner;
import java.util.StringTokenizer;

public class exercicio3 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um texto: ");
		String resp = entrada.nextLine();
		
		StringTokenizer resp2 = new StringTokenizer(resp);
		System.out.println(resp2.countTokens());
		
		entrada.close();
	}
}
