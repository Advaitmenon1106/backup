class Main{
  int x = 5;
}
class Hi{
    int x = 6;
}
public class Oops {
    public static void main(String[] args){
        Main newObj = new Main();
        Hi newObj2 = new Hi();
        System.out.println(newObj2.x);
        System.out.println(newObj.x);
        newObj.x = 12;
        System.out.println(newObj.x);
    }    
}