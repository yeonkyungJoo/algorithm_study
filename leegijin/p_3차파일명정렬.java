package leegijin;

import java.util.Arrays;

class p_3차파일명정렬 {
    static int i = 0;
    public static void main(String[] args) {
        String [] s = {"img12.png", "img10.png", "img02.png", "img1.png", "IMG01000000.GIF", "img2.JPG"};
        String [] tmp=solution(s);
        for(String t : tmp){
            System.out.println("t = " + t);
        }
    }

    public static String[] solution(String[] files) {
        Arrays.sort(files, (o1, o2) -> {
            System.out.println("o1 = " + o1);
            System.out.println("o2 = " + o2);
            String head1 = o1.split("[0-9]")[0].toLowerCase(); // head - number, tail 분리
            String head2 = o2.split("[0-9]")[0].toLowerCase();
            if (head1.equals(head2)) { // head 같은문자열인 경우
                String numTail1 = o1.substring(head1.length()); // number,tail 남김
                String numTail2 = o2.substring(head2.length());
                System.out.println("numTail2 = " + calNumber(numTail2));
                return Integer.parseInt(calNumber(numTail1)) - Integer.parseInt(calNumber(numTail2));
            } else {
                return head1.compareTo(head2);
            }
        });
        return files;
    }

    private static String calNumber(String numTail2) { //최대 5자리인 number 계산
        StringBuilder sb2 = new StringBuilder();
        for (char c : numTail2.toCharArray()) {
            if (Character.isDigit(c) && sb2.length() <= 5) {
                sb2.append(c);
            } else {
                return sb2.toString();
            }
        }
        return sb2.toString();
    }
}