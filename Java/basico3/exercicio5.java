package basico3;

import java.util.Scanner;

public class exercicio5 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um texto: ");
		String resp = entrada.nextLine();
		
		String resultado = resp.toUpperCase();
		System.out.println(resultado);
	}
}
