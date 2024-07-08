package basico3;

public class basico3_1 {
	public static void main(String[] args) {
		
		char caracteres[] = {'a','b','c'};
		String texto = new String(caracteres);
		System.out.println(texto);
		
		String str = "Hello";
		String resultado = str.replace("l","w");
		System.out.println(resultado);
		
		int tres = 3;
		String resultadoFinal = 3 + "palavra" + tres;
		System.out.println(resultadoFinal);
		
		String str2 = "Hello World";
		String resultado3 = str2.substring(6);
		System.out.println(resultado3);
		
		String resultado4 = str2.substring(3,8);
		System.out.println(resultado4);
		
		
		
	}
}
