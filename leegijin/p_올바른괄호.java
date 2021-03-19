package leegijin;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class p_올바른괄호 {
    public static void main(String[] args) {
        String s= "(())()";
        System.out.println(solution(s));
    }
    /* #  효율성 테스트 실패
    static boolean solution(String s) {
        boolean answer = true;
        ArrayList<Character> a = new ArrayList<>();
        for(int i=0; i<s.length() ; i++){
            if(s.charAt(i)=='('){
                a.add('(');
            }
            else if(s.charAt(i)==')' && a.size()!=0)
                a.remove(0);
            else{
                answer=false;
                break;
            }
        }
        if(a.size()!=0)
            answer=false;
        return answer;
    }
    */
    //성공
    static boolean solution(String s) {
        boolean answer = true;
        int count =0;
        for(int i=0; i<s.length();i++){
            if(s.charAt(i)=='('){
                count++;
            }
            else{
                if(count==0) {
                    answer=false;
                    break;
                }
                count--;
            }
        }
        if(count!=0)
            answer=false;
        return answer;
    }
}
