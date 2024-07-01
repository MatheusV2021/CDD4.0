package repeticoes;

import java.util.Scanner;

public class exercicio01 {
	public static void main(String[] args) {
		double num, rep, soma, nota, media;
		num = 0;
		rep = 0;
		soma = 0;
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Numero de alunos: ");
		num = entrada.nextInt();
		
		while (rep < num) {
			System.out.println("Nota: ");
			nota = entrada.nextInt();
			soma = soma + nota;
			++rep;
		}
		media = soma/num;
		
		System.out.println(media);
		
		entrada.close();
	}
}
