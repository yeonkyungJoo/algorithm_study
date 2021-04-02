package leegijin;

import java.util.Arrays;

public class p_구명보트 {
    public static void main(String[] args) {
        int [] people ={70, 50, 80, 50};
        int limit =100;
        System.out.println(solution(people,limit));
    }
    public static int solution(int[] people, int limit) {

        Arrays.sort(people);
        int count = 0, s = 0, l = people.length-1;

        while(s<=l) {
            if(people[s] + people[l] <= limit)
                s++;
            l--;
            count++;
        }
        return count;
    }

}
