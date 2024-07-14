//package test_package;
class Student_demo{
    int id;
    String name;
}

//Overriding requires inheritance
//Multiple children classes- most useful reason to ooverride

public class helloworld{

    static void f1(int h){//method overloading
        System.out.println("Value = " + h);
    }
    static void f1(String y){
        System.out.println("Hello " + y);
    }
    
    public static void main(String[] args){
        System.out.println("Hello world"); //ln prints a sentence THEN moves cursor to a new line
        System.out.println ("Hi");
        String h = "helloworld";
        System.out.println(h+ " " + "e" + " " + 2);
        float e = 12.7e4f;
        System.out.println(++e);
        System.out.println(h.length());
        String txt = "AB AB EFGHIJKLMNOPQRSTUVWXYZ";
        char[] arr1 = txt.toCharArray();
        System.out.println(arr1[0]);

        /*for (int c = 0; c<=100; c++){
            System.out.println(1);
        }*/
        f1("world");
        f1(2);
    }
}