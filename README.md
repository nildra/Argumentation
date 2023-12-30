Abstract Argumentation Solver
=============================

Run the software from the **src/** directory: `python3 script.py -p XX-YY -f FILE -a ARGS`  
- -f FILE : path to the file describing the AF  
      E.g. : `python3 script.py -p XX-YY -f ~/path/to/af.txt -a ARGS`
- -p XX-YY : 'VE-CO' or 'VE-ST' or 'DS-CO' or 'DC-CO' or 'DS-ST' or 'DC-CO'  
      E.g. : `python3 script.py -p VE-CO -f ~/path/to/af.txt -a ARGS`   
- -a ARGS : 'ARG1,ARG2,...ARGN' or 'ARG' or '[]'  
        To test the program with the empty set as an argument, put '[]' : `python3 script.py -p VE-CO -f path/to/af.txt -a []`  
        ARGS = unique ARG for the DS-YY and DC-YY options : `python3 script.py -p DS-CO -f path/to/af.txt -a b`  
        ARGS can be a sequence  of letters for the VE-YY options : `python3 script.py -p VE-CO -f path/to/af.txt -a b,d,e`  
        
