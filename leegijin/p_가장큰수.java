package leegijin;

import java.util.Arrays;
import java.util.Comparator;

public class p_가장큰수 {
    public static void main(String[] args) {
        int [] numbers = {6, 10, 2}; //6210
        int [] numbers1 ={3, 30, 34, 5, 9}; //9534330
        System.out.println(solution(numbers1));

    }
    public static String solution(int[] numbers) {
        String[] arr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++)
            arr[i] = String.valueOf(numbers[i]);

        Arrays.sort(arr, (o1, o2) -> (o2+o1).compareTo(o1+o2)); // 문자열 비교



        if(arr[0].equals("0")) return "0";

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            System.out.println("arr = " + arr[i]);
            sb.append(arr[i]);
        }
        return sb.toString();
    }
}
