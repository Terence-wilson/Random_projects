public class Abacus {
    public static void main(String[] original) {
        String[] origin = {"ooooooooo---", "ooooooooo---", "ooooooooo---", "ooooooooo---",
         "ooooooooo---", "ooooooooo---"};
         int val = Integer.parseInt(original[0]);
        String[] jerry = add(origin, val);
        for (String i: jerry) {
            System.out.println(i);
        }
    }
    public static String[] add(String[] original, int val) {
        int base = 100000;
        int abbyVal = 0;
        for (String dig: original) {
            abbyVal += (9-dig.indexOf("-")) * base;
            base = base/10;
        }
        int newVal = val + abbyVal;
        String gap = "---";
        String tick = "o";
        String[] finAbby = new String[6];
        String abbyStr;
        for (int i = 5; i >= 0; i--) {
        	int singleDig = newVal%10;
            newVal = (newVal-singleDig)/10;
            if (singleDig == 9) {
            	abbyStr = gap;
            } else {
                abbyStr = tick;
            }
            if (abbyStr == gap) {
                for (int j = 8; j >= 0; j--) {
                    abbyStr = abbyStr.concat(tick);
                    

                }
            } else {
            	for (int j = 8; j >= 0; j--) {
                	if (j != singleDig) {
                    	abbyStr = abbyStr.concat(tick);
                	} else {
                    	abbyStr = abbyStr.concat(gap);
                    }
                }
            }
            finAbby[i] = abbyStr;
        }
        return finAbby;
    }
}