public class MaxThread extends Thread{
    private Integer[]arr;
    public MaxThread(Integer[] arr){
        this.arr=arr;
    }
    public void run(){
        int max = arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i] > max){
                max=arr[i];
            }
        }
        System.out.println("Max value: " +max);
    }
}
