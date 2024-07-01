package repeticoes;

public class exercicio03 {
	public static void main(String[] args) {
		int num = 0;
		int num2 = 0;
		
		while (num < 100) {
			if (num % 2 != 0) {
				System.out.print(num+" ");
			}
			++num;
			}
		System.out.println(" ");
		
		while (num2 < 100) {
			if (num2 % 2 == 0) {
				System.out.print(num2+" ");
			}
			++num2;
		}
	}
}
