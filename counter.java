public class Counter{
    private static int count=0;
    public counter(){
        count++;
    }
    public static int getcount(){
      return count;
    }
    

public static void main(String[] args){
    Counter c1=new Counter();
    Counter c2=new Counter();
    Counter c3=new Counter();
    System.out.println("count"+c2.count);
    System.out.println("count"+Counter.getcount());}
}