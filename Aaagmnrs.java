import java.util.ArrayList;
import java.util.List;

import java.util.Arrays;

public class Aaagmnrs {
    public static void main(String[] args) {
        String[] poop = anagrams(args);
        for (String i : poop) {
            System.out.println(i);
        }
    }

    public static String[] anagrams(String[] phrases) {
        List<String> remPhrases = new ArrayList<String>();
       for (String phrase: phrases) {
            int count;
            if (remPhrases == null) {
                count = 0;
            } else {
                count = 0;
                String tempPhrase = phrase.replace(" ", "").toLowerCase();
                char[] temphrase = tempPhrase.toCharArray();
                Arrays.sort(temphrase);
                temphrase.toString();
                for (String rem: remPhrases) {
                    String tempRem = rem.replace(" ", "").toLowerCase();
                    char[] tempem = tempRem.toCharArray();
                    Arrays.sort(tempem);
                    tempem.toString();
                    if (Arrays.equals(tempem, temphrase)) {
                        count++;
                        break;                        
                    } 
                }                
            }
            if (count == 0) {
                remPhrases.add(phrase);
            } else {
                count = 0;
            }
        }
        return remPhrases.toArray(new String[remPhrases.size()]);
    }
}