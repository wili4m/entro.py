# entro.py
This is another password generator that uses entropy analysis to create strong passwords via CLI.

## How it works:

**Entro.py** is a tool that generates passwords. The default output seems like this:

```
--------------------------------------------------
Automagically generated passwords:
--------------------------------------------------
1: yO`MhOp]PiM7fiVxpjNtmEGKI8f_gsH\d7%Ati_CU-W2}rB*Df
2: MDE23KtnDXT~?ritQAK&~:7Ve53&fZ}P*R]z4KGk6fb6SF9u<2
3: AhYg(J"c6MqRlocxpNqY:UQv@B\J5V`AT2:UkvS3z&8wHa}wy[
4: !Rpvu{9Fd7^7|EiZ7UEO%e)\}}@z'vq*/3awrm\E2)jE-~4OLo
5: K1q:EeFEJ>},$xk;8Og/#s3<,5sEzc4|&1s%u3iqg^%*.R(\.'

Would you like to specify the password format? [y/N]:
```

In this prompt, the user can create a password by specifying specific criteria:

```<<< Would you like to specify the password format? [y/N]:```

The following options will be displayed one at time:

```
<<< Amount of characters:
<<< Include numbers? [Y/n]:
<<< Include uppercase characters? [Y/n]:
<<< Include symbols? [Y/n]:
```

Next, the tool will generate a password based on user preferences and analyze its entropy to classify it as Strong, Medium, or Weak.

```
--------------------------------------------------
>>> Password: ?MhT1%1AGxDxLlGyHMC:|#%V+IH?`HEmS,dQuf4&#~@<jV=#bJ
>>> Strength: Strong
--------------------------------------------------
```

## Backlog:

* Create passwords in a single line.
* Accept parameters to generate passwords in a specific format.
* Choose which symbols will be used in the password.
