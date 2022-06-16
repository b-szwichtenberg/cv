import java.util.ArrayList;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Map<String,String> m = new HashMap<String,String>();
        m.put("Poland","Warsaw");
        m.put("Italy","Rome");
        m.put("France","Paris");
        Scanner input = new Scanner(System.in);
        for (Map.Entry<String, String> e : m.entrySet()) {
            System.out.println("Capital of "+e.getKey()+":");
            String a = input.next();
            if(a.equals(e.getValue())){
                System.out.println("CORRECT");
            }else{
                System.out.println("Correct answer:"+e.getValue());
            }
        }
        }
    }
