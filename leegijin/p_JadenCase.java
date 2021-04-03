package leegijin;

public class p_JadenCase {
    public static void main(String[] args) {
        String s = "3people unFollowed me";
        System.out.println(solution(s));
    }
    public static String solution(String s) {
        String[] arr = s.split(" ");
        if(s.substring(s.length() - 1, s.length()).equals(" ")) {
            arr[arr.length-1] += " ";
        }
        String answer = "";
        int cnt = 0;
        char t;
        for (String tmp : arr) {
            cnt++;
            for (int i = 0; i < tmp.length(); i++) {
                t = tmp.charAt(i);
                if (i == 0)
                    answer += tmp.valueOf(t).toUpperCase();
                else if(t==' ') {
                    answer +=" ";
                }
                else
                    answer += tmp.valueOf(t).toLowerCase();
            }
            if (cnt != arr.length)
                answer += " ";

        }
        return answer;

    }
}
