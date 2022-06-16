import java.util.Arrays;
public class MyThread extends Thread {
    public int[]arr;
    public MyThread(int[] arr){
        this.arr=arr;
    }
    public void run() {
        Arrays.sort(arr);
        System.out.println("Minimum value is: "+arr[0]);
    }
}
