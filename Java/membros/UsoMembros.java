package membros;

public class UsoMembros {
	public static void main(String[] args) {
		DataNascimento dt = new DataNascimento();
		DataNascimento dt2 = new DataNascimento();
		dt.dia = 12;
		dt.mes = 02;
		dt.ano = 1991;
		
		dt2.dia = 25;
		dt2.mes = 01;
		dt2.ano = 1992;
		
		System.out.printf("A data de nascimento "+"é: %d / %d / %d \n",dt.dia,dt.mes,dt.ano);
		
		System.out.printf("A data de nascimento "+"é: %d / %d / %d \n",dt2.dia,dt2.mes,dt2.ano);

	}
}
