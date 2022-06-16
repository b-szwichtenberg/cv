public class MyThread2 extends Thread{
    public void run(){
        try{
            Thread.sleep(1000);
        }
        catch(InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("MyThread2 is running");
    }
}
