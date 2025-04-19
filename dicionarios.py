#!/usr/bin/env python
# coding: utf-8

# ### Definição de Dicionário: É um objeto que representa a coleção de um ou mais objetos. Cada objeto tem sua chave e seu valor. Assim, para acessar um valor de um determinado objeto, basta chamarmos sua chave. Os dicionários são iniciados e terminados por chaves { }

# #### Criando dicionários

# In[1]:


dict1 = {'chave1': 'valor1',
         'chave2': 'valor2'}


# In[2]:


dict1


# In[3]:


type(dict1)


# In[4]:


dict2 = dict(a=1,
            b=2,
            c=3,
            d='a')


# In[5]:


dict2


# In[6]:


dict3 = dict([('a',1),
             ('b',2),
             ('c',3)])


# In[7]:


dict3


# In[9]:


dict4 = {'chave1': ['nome', 'idade', 'cidade'],
         'chave2': ['Samuel', 24, 'São Paulo']}


# In[10]:


dict4


# In[11]:


dict5 = {'id': [1,2,3],
        'user': {'nome':['Caio', 'Rafael', 'Pedro'],
                    'idade': [29,30,31]}}


# In[12]:


dict5


# In[13]:


dict6 = dict(zip(['chave1', 'chave2','chave3'],
                ['valor1','valor2','valor3']))


# In[14]:


dict6


# #### Acessando valores do dicionário

# In[16]:


dict1


# In[17]:


dict1['chave1']


# In[18]:


dict1.get('chave2')


# In[19]:


dict1.get('Chave1','Não existe essa chave!')


# In[20]:


dict1.get(list(dict1)[1])


# In[21]:


for chave in dict1.keys():
    print(chave, dict1[chave])


# In[23]:


for chave,valor in dict1.items():
    print(chave,valor)


# #### Juntando Dicionários

# In[24]:


dict1


# In[25]:


dict2


# In[28]:


dict1.update(dict2)


# In[29]:


dict1


# In[30]:


dict1['nova chave'] = 100


# In[31]:


dict1


# In[32]:


dict1.update({'outra chave': 'outro valor'})


# In[33]:


dict1


# In[35]:


{**dict2,**dict3}


# #### Verificando se um valor pertence a chave

# In[36]:


dict3


# In[37]:


1 == dict3['a']


# #### Métodos

# In[38]:


dict3.clear()


# In[39]:


dict3


# In[40]:


dict100 = dict3.copy()


# In[41]:


dict100


# In[42]:


dict4


# In[43]:


dict4.pop('chave1')


# In[44]:


dict4


# In[45]:


dict6


# In[46]:


dict6.popitem()


# In[47]:


dict6


# In[ ]:




