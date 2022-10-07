import java.util.*;
class program1
{
    //Method used to solve the program
    public static void solve(HashMap<Integer,Integer> g_map, int numOfP)
    {
        //taking the size of the hashmap passed as parameters
        int sz = g_map.size();
        Integer myNum = numOfP;
        boolean flag = true;
        //Iterating our way out thorugh the hashmap
        for(int i = 0; i < sz; i++)
        {
            if(myNum == g_map.get(i))
                System.out.println("Planet exists in galaxy "+i);   
                flag = false;
                break;
        }
        if(flag == false)
            System.out.println("Planet doesn't exist");
    }
    public static void main(String[] args) 
    {
        //Using a HashMap to store Galaxy Number : Planet Number 
        HashMap<Integer, Integer> map = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        System.out.println(">> Enter number of galaxies in the universe");
        //Taking the number of galaxies input
        int n = sc.nextInt();
        //Checking for constraints and terminating if not matched

        if(n < 0 || n > 1000)
        {
            System.out.println("Please maintain the constraints");
            System.exit(1);
        }

        for(int i = 0; i < n;i++)
        {
            //Taking input how many planets in each galaxy
            System.out.println(">> Enter the number of planets in galaxy "+i);
            int a = sc.nextInt();
            //Terminating code if not matching else putting value in hashmap
            if(a >= 20 && a <= 20000)
            {
                map.put(i,a);
            }

            else
            {
                System.out.println("Please follow the constraints");
                System.exit(1);
            }
        }
        //Similarly inputting t and checking for constraints
        System.out.println(">> Enter searching number for planets");
        int t = sc.nextInt();
        if(t<0 || t>20000)
        {
            System.out.println("Please follow the constraints");
            System.exit(1);
        }
        //Invoking void method solve()
        solve(map,t); 
    }
}