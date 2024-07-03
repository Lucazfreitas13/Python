print('\033[0;30;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[1;35;43mTESTE\033[m')
print('\033[30;42mTESTE\033[m')
print('\033[7;97mTESTE\033[m')
print('\033[0;97;40mTESTE\033[m')
print('\033[7;97m-=-\33[m'*25)

nome='Lucas'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[1;34m',nome,'\033[m'))

nome1='Lucas'
cores={'limpa':'\033[m',
      'azul':'\033[34m',
      'amarelo':'\033[33m',
      'pretoEbranco':'\033[0;30;107m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoEbranco'],nome,cores['limpa']))







