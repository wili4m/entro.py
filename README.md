# entro.py
This is another password generator that uses entropy analysis to create strong passwords via CLI.

How it works:

**Entro.py** is a tool that generates passwords:

```
--------------------------------------------------
Automagically generated passwords:
--------------------------------------------------
1: yO`MhOp]PiM7fiVxpjNtmEGKI8f_gsH\d7%Ati_CU-W2}rB*Df
2: MDE23KtnDXT~?ritQAK&~:7Ve53&fZ}P*R]z4KGk6fb6SF9u<2
3: AhYg(J"c6MqRlocxpNqY:UQv@B\J5V`AT2:UkvS3z&8wHa}wy[
4: !Rpvu{9Fd7^7|EiZ7UEO%e)\}}@z'vq*/3awrm\E2)jE-~4OLo
5: K1q:EeFEJ>},$xk;8Og/#s3<,5sEzc4|&1s%u3iqg^%*.R(\.'
```
You always have the chance to create a password according to your criteria:

```<<< Would you like to specify the password format? [y/N]:```

The following prompt will be displayed, one item per time:

```
<<< Amount of characters:
<<< Include numbers? [Y/n]:
<<< Include uppercase characters? [Y/n]:
<<< Include symbols? [Y/n]:
```

Next, the tool will create a password as you wish and analyze if the password is secure or not:

```
--------------------------------------------------
>>> Password: ?MhT1%1AGxDxLlGyHMC:|#%V+IH?`HEmS,dQuf4&#~@<jV=#bJ
>>> Strength: Strong
--------------------------------------------------
```
