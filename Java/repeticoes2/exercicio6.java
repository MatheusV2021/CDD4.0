package repeticoes2;

public class exercicio6 {
	public static void main(String[] args) {
		int soma3 = 0;
		int soma5 = 0;
		
		for (int x = 0; x<=20; x++) {
			if (x % 3 == 0) {
				System.out.print(x+" ");
				soma3 += x;
			}
		}
		
		System.out.println(" ");
			
		for (int i = 0; i<=20;i++) {
			if (i % 5 == 0) {
				System.out.print(i+" ");
				soma5 += i;
			}
		}
		
		int soma = soma3+soma5;
		System.out.println(" ");
		System.out.println(soma3);
		System.out.println(soma5);
		System.out.println(" ");
		System.out.println(soma);
		}
	}

