package membros;


public class faculdade {
	public static void main(String[] args) {
		aluno a1 = new aluno("Matheus", 22);
		a1.matricula = "71165691469";
		
		professor p1 = new professor("Wellington",60);
		p1.salario = 20000;
		p1.disciplina = "Programação";
		
		funcionario f1 = new funcionario("Daniel",20);
		f1.salario = 10000;
		f1.cargo = "Monitor";
		
		System.out.printf("Aluno: "+a1.nome+"\nIdade: "+a1.idade+"\nMatricula: "+a1.matricula+"\n");
		System.out.println("--------------------------");
		System.out.printf("Professor: "+p1.nome+"\nIdade: "+p1.idade+"\nSalario: "+p1.salario+"\nDisciplina: "+p1.disciplina+"\n");
		System.out.println("--------------------------");
		System.out.printf("Funcionario: "+f1.nome+"\nIdade: "+f1.idade+"\nSalario: "+f1.salario+"\nCargo: "+f1.cargo);
	}
}
