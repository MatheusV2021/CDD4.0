package construtor;
import java.util.Scanner;


public class acoes {
		public boolean ligando = false;
	    public boolean verificando = false;
	    public boolean desligando = false;
	    
	    public void ligar() {
	        if (!ligando && !verificando && !desligando) {
	            ligando = true;
	            System.out.println("Ligando...");
	        } else {
	            System.out.println("Outra ação está sendo executada. Por favor, aguarde ou pare a ação atual.");
	        }
	    }
	    
	    
	}

