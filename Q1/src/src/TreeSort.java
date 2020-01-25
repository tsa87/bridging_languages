import java.util.List;
import java.util.TreeSet;

public class TreeSort {

    public TreeSort(List<Long> data)
    {
        TreeSet<Long> tree=new TreeSet<>();

        for(long x: data)
            tree.add(x);

        for(long x: tree)
            System.out.print(x+" ");

        System.out.println();
    }
}
