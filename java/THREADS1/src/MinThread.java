public class MinThread extends Thread{
    private Integer[]arr;
    public MinThread(Integer[] arr){
        this.arr=arr;
    }
    public void run(){
        int min = arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i] < min){

                min=arr[i];
            }
        }
        System.out.println("Min value:" + min);
    }
}
