package leegijin;

import java.io.*;
import java.util.*;


public class p_1092배 {

    static int N, M;
    static ArrayList<Integer> crane = new ArrayList<>();
    static ArrayList<Integer> box = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            crane.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            box.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(crane, new Comparator<Integer>() {

            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.compareTo(o1);
            }
        });
        Collections.sort(box, new Comparator<Integer>() {

            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.compareTo(o1);
            }
        });

        System.out.println(calc());
    }

    private static int calc() {
        if (crane.get(0) < box.get(0)) {
            return -1;
        }

        int time = 0;
        while (box.size() != 0) {
            int idx = 0;
            int temp = 0;
            while (idx < N) {
                if (temp == box.size()) break;
                if (box.get(temp) <= crane.get(idx)) {
                    box.remove(temp);
                    idx++;
                } else if (box.get(temp) > crane.get(idx)) {
                    temp++;
                }
            }
            time++;
        }
        return time;
    }
}
