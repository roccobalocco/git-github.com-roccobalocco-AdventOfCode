import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Sette{
    
    private class Tree{
        Map<String, Long> nodes = new HashMap<String, Long>();
        String cwd = "";

        Tree(){}

        public void moveDown(){
            if (cwd.equals("/"))
                return;
            cwd = cwd.substring(0, cwd.lastIndexOf("/"));
            cwd = cwd.substring(0, cwd.lastIndexOf("/") + 1);
        }

        private String moveDown(String cwd){
            String tmp = cwd.substring(0, cwd.lastIndexOf("/"));
            tmp = tmp.substring(0, tmp.lastIndexOf("/") + 1);
            return tmp;
        }

        public void moveUp(String where){
            cwd += where + "/";
        }

        public void moveHome(){
            cwd = "/";
        }

        public void addNode(String directory){
            nodes.put(cwd + directory + "/", (long) 0);
        }


        public void updateNode(Long datas){
            nodes.replace(cwd, getValue(cwd) + datas);
            updateUp(cwd);
        }

        public void updateNode(String cwd, Long datas){
            if (cwd.equals("/"))
                return;
            nodes.replace(cwd, getValue(cwd) + datas);
            updateUp(cwd);
        }


        private void updateUp(String absolutePath) {
            if (absolutePath.equals("/") || absolutePath.length() == 0)
                return;
            Long tmp = getValue(absolutePath);
            absolutePath = moveDown(absolutePath);
            updateNode(absolutePath, tmp);
        }

        private Long getValue(String cwd) {
            if (cwd.equals("/"))
                return (long) 0;
            return nodes.get(cwd);
        }

        public long getSum(){
            long tot = 0;
            for (String key : nodes.keySet()){
                if (nodes.get(key) <= 100000 && nodes.get(key) > 0){
                    tot += nodes.get(key);
                }
            }
            return tot;
        }

        public long getLowest(long limit){
            long tot = 0;
            for (String key : nodes.keySet()){
                if (nodes.get(key) <= limit && tot > nodes.get(key)){
                    tot = nodes.get(key);
                }
            }
            return tot;
        }
        public long totSum(){
            long tot = 0;
            for (String key : nodes.keySet()){
                tot += nodes.get(key);
                System.out.println(key + "--" + nodes.get(key));
            }
            return tot;
        }
    }
    private static void initializeTree(Tree tree, Scanner scanner){
        String s;
        Long sizeList = (long) 0;
        ArrayList<String> dirList = new ArrayList<>();
        while(scanner.hasNext()){
            s = scanner.nextLine();
            if (s.substring(2, 4).equals("cd")){
                if (dirList.size() > 0){
                    for (String dir : dirList)
                        tree.addNode(dir);
                    dirList = new ArrayList<>();
                }
                if (sizeList > 0){
                    tree.updateNode(sizeList);
                    sizeList = (long) 0;
                }
                String tmp = s.substring(5);
                switch(tmp){
                    case "..":
                        tree.moveDown();
                        break;
                    case "/":
                        tree.moveHome();
                        break;
                    default:
                        tree.moveUp(tmp);
                }
            }else if (s.substring(2, 4).equals("ls")){
                if (dirList.size() > 0){
                    for (String dir : dirList)
                        tree.addNode(dir);
                    dirList = new ArrayList<>();
                }
                if (sizeList > 0){
                    tree.updateNode(sizeList);
                    sizeList = (long) 0;
                }
                sizeList = (long) 0;
                dirList = new ArrayList<>();
            }else{
                String[] tmp = s.split(" ");
                if (tmp[0].equals("dir"))
                    dirList.add(tmp[1]);
                else
                    sizeList += Long.valueOf(tmp[0]);
            }
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        File f = new File("./in.txt");
        Scanner s = new Scanner(f);
        Sette sette = new Sette();
        Tree tree = sette.new Tree();
        initializeTree(tree, s);
        //Modified for level2, still not working. Fix it asap
        System.out.println(tree.totSum());
        //System.out.println(tree.getLowest(1320487000623));
    }
}