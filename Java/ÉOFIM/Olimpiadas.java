package ÉOFIM;

import java.util.Scanner;

public class Olimpiadas {
	public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	Triatleta triatleta = new Triatleta();
	String comando;

	System.out.println("Digite uma ação: ");

	while (true) {
		comando = scanner.nextLine().trim().toLowerCase();

		switch (comando) {
			case "nadar":
				triatleta.nadar();
				break;
				
			case "correr":
				triatleta.correr();
				break;
				
			case "pedalar":
				triatleta.pedalar();
				break;
				
			case "descansar":
				triatleta.descansar();
				break;
				
			case "sair":
				System.out.println("Encerrando o programa...");
                scanner.close();
                return;
				default:
					System.out.println("Comando inválido. Por favor, digite 'comer', 'andar', 'dormir', 'parardecomer', 'parardeandar', 'parardedormir' ou 'sair'.");
	                       
	            }
	        }
	}
}
