package leegijin;

import java.util.ArrayList;

public class p_3차방금그곡 {
    public static void main(String[] args) {
        String m ="ABC";
        String [] musicinfos = {"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"};
        System.out.println(solution(m,musicinfos));
    }
    /*
    방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
    네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
    각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
    음악이 00:00를 넘겨서까지 재생되는 일은 없다.
    조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
    조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
     */
    public static String solution(String m, String[] musicinfos){
        String answer = "(None)";
        int maxtime = 0;
        for(int i = 0; i<m.length();i++){
            m = m.replace("A#","a");
            m = m.replace("C#","c");
            m = m.replace("D#","d");
            m = m.replace("F#","f");
            m = m.replace("G#","g");
            m = m.replace("E#","e");
        }

        for(int i = 0; i< musicinfos.length;i++) {
            String[] tmp = musicinfos[i].split(",");

            tmp[3] = tmp[3].replace("A#","a");
            tmp[3] = tmp[3].replace("C#","c");
            tmp[3] = tmp[3].replace("D#","d");
            tmp[3] = tmp[3].replace("F#","f");
            tmp[3] = tmp[3].replace("G#","g");
            tmp[3] = tmp[3].replace("E#","e");


            String[] stime = tmp[0].split(":");
            String[] etime = tmp[1].split(":");

            int hour = Integer.parseInt(etime[0]) - Integer.parseInt(stime[0]);
            int min = Integer.parseInt(etime[1]) - Integer.parseInt(stime[1]) + (hour * 60);

            String melody = "";
            for(int j = 0; j<min;j++){
                melody += tmp[3].charAt(j%tmp[3].length());
            }

            if(melody.contains(m)){
                if(maxtime < melody.length()){
                    maxtime = melody.length();
                    answer = tmp[2];
                }
            }
        }
        return answer;
    }
}
