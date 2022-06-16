import java.util.*;
public class Main {
    public static void main(String[] args) {
        ArrayList<String> arrL = new ArrayList<String>();
        arrL.add("Sweden");
        arrL.add("Japan");
        arrL.add("Kuba");
        arrL.add("Spain");

        Iterator<String> it = arrL.iterator();
        while(it.hasNext()) {
            it.remove();
        }

        System.out.println("ArrayList size: "+ arrL.size());
        for (int i = 0; i < arrL.size(); i++) {
            System.out.println(arrL.get(i));
        }
    }
}

