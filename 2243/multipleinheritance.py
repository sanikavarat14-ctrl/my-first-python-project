interface A{
    
    default void display(){
        
        System.out.println("Interface A display");
    }
}

interface B{
    
    default void display(){
        
        System.out.println("Interface B display");
    }
}

class C implements A, B{
    
    @Override
    public void display(){
        
        // Resolving conflict
        A.super.display();
        B.super.display();
        System.out.println("Class C display");
    }
}

public class Main {
    public static void main(String[] args){
        
        C obj = new C();
        obj.display();
    }
}
