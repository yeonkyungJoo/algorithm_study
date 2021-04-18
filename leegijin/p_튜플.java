package leegijin;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class p_튜플 {
    public static void main(String[] args) {
        String s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
        int a [];
        a=solution(s);
        for(int i =0; i<a.length ; i++) {
            System.out.println(a[i]);
        }

    }
    public static int[] solution(String s) {
        s = s.substring(2, s.length()-2).replace("},{", "-");

        String [] arr = s.split("-");
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.length() - o2.length();
            }
        });

        ArrayList<Integer> list = new ArrayList<>();
        for(String temp : arr) {
            String [] val = temp.split(",");

            for(int i=0 ; i<val.length ; i++) {
                int num = Integer.valueOf(val[i]);

                if(!list.contains(num)) {
                    list.add(num);
                }
            }
        }

        int [] answer = new int[list.size()];
        for(int i=0 ; i<list.size() ; i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
    //"{{2},{2,1},{2,1,3},{2,1,3,4}}"

}
