import discord
import random
import asyncio

client = discord.Client()
prefixo = '.'
colorg = 0x008f0a
colorr = 0xa80000
colorb = 0x000875
colorp = 0x6a0094
colory = 0xc79902
colorc = 0x00e8cd
colord = 0x000000
cooldownmembers = []


gifshug = ['https://cdn.discordapp.com/attachments/743833882285178912/744033860580409344/tenor_3.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744033828900700161/7cc9a47825a9fd104554904df6937ddd5caccbbe_hq.gif',
           'https://cdn.discordapp.com/attachments/743833882285178912/744033807010889758/anime-hug.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744229992396750958/1cfc7c958a8280ada0a9f8c06bd98428b43d7237_hq.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744230014286823484/027e0ab608f8b84a25b2d2b1d223edec.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744330929966678046/tenor_5.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744331309979009145/5aac6270d9c29bb8c590c8d8c8162a21.gif']
gifsdance = ['https://cdn.discordapp.com/attachments/591971202277310489/743974836757594212/Pug-1.gif',
             'https://cdn.discordapp.com/attachments/743833882285178912/744240600118984724/Konosubadancinggifscenterbig3httpsmyanimelistnetanime30831konosubarashiisekainishukufukuwobig3center.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744241077564997673/PotableDarkAkitainu-max-1mb.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744245685272051792/970e8854598ee99134e37dfab4d26ee2.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744335161029689464/giphy_2.gif']
gifspunch = ['https://cdn.discordapp.com/attachments/743833882285178912/744013228933382276/1479925765_tumblr_ndjxf7V2FU1s4cujlo1_500.gif',
             'https://cdn.discordapp.com/attachments/743833882285178912/744320798155735181/giphy_1.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744329188554833930/1f79030e75916b4d57c5b0f82e5a2446.gif']
gifsaffection = ['https://cdn.discordapp.com/attachments/743833882285178912/744328922669383751/5c979c1b83cae4d8d14c53c2a28e99984d620e3d_hq.gif',
                 'https://cdn.discordapp.com/attachments/743833882285178912/744329562116325436/giphy.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744332621017907244/b6d0903e0d54e05bb993f2eb78b39778.gif']
gifsbite = ['https://cdn.discordapp.com/attachments/660977416176533548/743259989426176020/e6c7439f45d42ce064309c95256da876e362fc1a_00.gif',
            'https://cdn.discordapp.com/attachments/743833882285178912/744338839975493692/ConsiderateFrighteningAzurevasesponge-size_restricted.gif', 'https://cdn.discordapp.com/attachments/743833882285178912/744338849479786607/6a89627d423c7def5703c031e610fa353bcb1882_00.gif', 'https://cdn.discordapp.com/attachments/531892331503288329/744346174781128714/tenor.gif']
gifsrejection = [
    'https://cdn.discordapp.com/attachments/743833882285178912/744334826051469342/0po2hturqba51.gif']


menheraaffection = ['https://cdn.discordapp.com/attachments/743984348386164836/745416392248918076/a67cd6a98f6b194bcdd905b30a55547e14393123r1-370-300_00.gif',
                    'https://cdn.discordapp.com/attachments/743984348386164836/745416394232955010/7d86289219df06a008178e25f686c0d7.gif', 'https://cdn.discordapp.com/attachments/743984348386164836/745416415611453460/c2631d8fab90cca2738ed77236fbef45.gif', 'https://cdn.discordapp.com/attachments/743984348386164836/745466026040230009/81fdf219ef42c1508799f27c1e5589ed.gif']
menherarejection = ['https://cdn.discordapp.com/attachments/743984348386164836/745416723938672670/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f.gif',
                    'https://cdn.discordapp.com/attachments/743984348386164836/745416728766578908/1697a249f70bfb55a7fc49b0175807d8.gif', 'https://cdn.discordapp.com/attachments/743984348386164836/745464049562812426/25354264_170x100.gif', 'https://cdn.discordapp.com/attachments/743984348386164836/745465268611842099/hyung-i-want-to-play-14884406-161120181341.gif']
lofilinks = ['https://www.youtube.com/watch?v=CyD1OKsd-Tk&list=PLbBllkL2l4nC7GCXonugSbs9rkuCXgsA5&index=13&t=0s',
             'https://www.youtube.com/watch?v=Xyj0Mq-YdUY', 'https://www.youtube.com/watch?v=A7Wo0MnC4z8', 'https://www.youtube.com/watch?v=6ZhJjRBnWYk', 'https://www.youtube.com/watch?v=CN_NPmKjWDM', 'https://www.youtube.com/watch?v=AzV77KFsLn4', 'https://www.youtube.com/watch?v=vcj2k113OzE']


# jokes = ['O que o pato falou pra pata?',
#          'Por que o pinheiro nunca se perde na floresta?'
# jokesrep= ['"Vem quá"', 'Porque ele tem uma pinha']
replies = [', espere alguns segundos 🙃', ', tá com pressa? Faz miojo 🍜',
           ', é muita pressão aaa 🤯', ', vai com calma aí 🥴', ', preciso de um tempinho 🥺', ', de novo? 😠']
welcomer = [', seja bem-vindo ao servidor do NOISE', ', boas-vindas e fique a vontade', ', é um prazer recebê-lo aqui',
            ', seja bem-vindo, mas... você trouxe café junto com você?', ', antes tarde do que nunca']
goodbyer = [', nunca é um adeus', ', até a próxima', ', foi bom enquanto durou', ', mas voce já vai?',
            ', sua saída é lamentável... hmmmmmm lámen', ', entendo, não estávamos dando certo', ' já vai tarde']
repliesaff = ['Obrigada pelo carinho, mestre', 'Você é o melhor mestre do mundo',
              'Como posso retribuir? Que tal um cafézinho? OU UMA PIZZA?']
replieshug = ['Obrigada pelo abraço, mestre', 'Você é o melhor mestre do mundo',
              'Como posso retribuir? Que tal um cafézinho? OU UMA PIZZA?', 'Posso lhe dar outro abraço?']
repliesrej = ['Huh? Quem é você?', 'Apenas meus mestres têm este direito', 'Huh? Você não é meu mestre',
              'Se você me der uma lasanha... eu posso até pensar no caso...', 'DISTANCIAMENTOOO']


@ client.event
async def on_ready():
    print('oi')
    print(client.user.name)


@ client.event
async def on_message(message):
    if message.content == prefixo + 'oi':
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colory)
            embedmessage.set_author(
                name=message.author.name + random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)
        else:
            await asyncio.sleep(1)
            await message.channel.send('Olá, tudo bem?')
            await asyncio.sleep(1)
            await message.channel.send('Meu nome é ' + client.user.name + '.')
            await asyncio.sleep(1)
            await message.channel.send(f'Se precisar de algo, utilize o comando: ***{prefixo}ajuda*** que lhe mostrarei as opções.')

        cooldownmembers.append(message.author.id)
        await asyncio.sleep(10)
        cooldownmembers.remove(message.author.id)

    if message.content.lower().startswith(prefixo + 'ajuda'):
        await message.channel.send(f"""Você pode escolher entre as opções qualquer uma delas:
    **{prefixo}comandos** ➔ lhe mostrarei a quais comandos eu obedeço neste servidor
    **{prefixo}lofi** ➔ lhe mandarei um link de um lofi aleatório""")

    # if message.content.lower().startswith(prefixo + 'me conte uma piada'):
    #     await message.delete()
    #     await message.author.send(random.choice(jokes))
    #     await asyncio.sleep(5)
    #     await message.author.send(random.choice(jokesrep))

    if message.content.lower().startswith(prefixo + 'lofi'):
        await message.delete()
        await message.author.send('Trouxe um lofi para você! Espero que goste 😄 ' + random.choice(lofilinks))

    if message.content.lower().startswith(prefixo + 'comandos'):
        await message.delete()
        await message.author.send("""```COMANDOS PARA O BOT MENHERA

.oi
.cargo
.dançar
.avatar  ➔  # para ver seu próprio avatar; caso queira ver o avatar de outra pessoa, mencione o usuário desejado após o comando
.bater  ➔  mencione alguém
.fazer carinho  ➔  mencione alguém
.rejeitar carinho ➔  mencione alguém
.morder  ➔  mencione alguém
.abraçar  ➔  mencione alguém

Esta mensagem será apagada em 3 dias. Caso desejar rever os comandos após a exclusão, aplique o comando novamente em qualquer canal disponível no servidor NOISE.
```
""", delete_after=259200)

    if message.content.startswith(prefixo + 'avatar'):
        await message.delete()
        try:
            user = message.mentions[0]
            embedmessage = discord.Embed(
                color=colorc, description=('avatar de ' + user.mention))
            embedmessage.set_image(url=user.avatar_url)
            await message.channel.send(embed=embedmessage, delete_after=10)
        except:
            embedmessage = discord.Embed(color=colorc, description=(
                'avatar de ' + message.author.mention))
            embedmessage.set_image(url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage, delete_after=10)

            cooldownmembers.append(message.author.id)
            await asyncio.sleep(5)
            cooldownmembers.remove(message.author.id)

    # if message.content.lower() == prefixo + 'canal noise':
    #     await message.channel.send('https://www.youtube.com/channel/UCCHuEAmWRQTFBEqBaL752uQ')

    # if message.content.lower() == prefixo + 'canal nightlight':
    #     await message.channel.send('https://www.youtube.com/channel/UCNk6wmmxQ0N_zA85Aegpkyg')

    if message.content.startswith(prefixo + 'abraçar'):
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colord)
            embedmessage.set_author(name=message.author.name +
                                    random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)
        else:
            user = message.mentions[0]
            if user == client.user:
                pass
            else:
                embedmessage = discord.Embed(color=colorb, description=(
                    message.author.mention + ' abraçou ' + user.mention))
                embedmessage.set_image(url=random.choice(gifshug))
                await message.channel.send(embed=embedmessage)

            cooldownmembers.append(message.author.id)
            await asyncio.sleep(5)
            cooldownmembers.remove(message.author.id)

    if message.content.lower().startswith(prefixo + 'abraçar'):
        adm = message.author.guild.get_role(829909356215926825)
        if user == client.user:
            if adm in message.author.roles:
                embedmessage = discord.Embed(
                    color=colorc, description=(random.choice(replieshug)))
                embedmessage.set_image(url=random.choice(menheraaffection))
                await message.channel.send(embed=embedmessage)
            else:
                embedmessage = discord.Embed(
                    color=colord, description=(random.choice(repliesrej)))
                embedmessage.set_image(url=random.choice(menherarejection))
                await message.channel.send(emmbed=embedmessage)

    if message.content.startswith(prefixo + 'bater'):
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colord)
            embedmessage.set_author(
                name=message.author.name + random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)
        else:
            user = message.mentions[0]
            embedmessage = discord.Embed(color=colorb, description=(
                message.author.mention + ' bateu em ' + user.mention))
            embedmessage.set_image(
                url=random.choice(gifspunch))
            await message.channel.send(embed=embedmessage)

            cooldownmembers.append(message.author.id)
            await asyncio.sleep(5)
            cooldownmembers.remove(message.author.id)

    if message.content.lower() == prefixo + 'dançar':
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colord)
            embedmessage.set_author(
                name=message.author.name + random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)

        else:
            embedmessage = discord.Embed(color=colorb, description=(
                message.author.mention + ' está dançando'))
            embedmessage.set_image(url=random.choice(gifsdance))
            await message.channel.send(embed=embedmessage)

        cooldownmembers.append(message.author.id)
        await asyncio.sleep(3)
        cooldownmembers.remove(message.author.id)

    if message.content.startswith(prefixo + 'fazer carinho'):
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colord)
            embedmessage.set_author(
                name=message.author.name + random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)
        else:
            user = message.mentions[0]
            if user == client.user:
                pass
            else:
                embedmessage = discord.Embed(color=colorb, description=(
                    message.author.mention + ' fez carinho em ' + user.mention))
                embedmessage.set_image(url=random.choice(gifsaffection))
                await message.channel.send(embed=embedmessage)

                cooldownmembers.append(message.author.id)
                await asyncio.sleep(5)
                cooldownmembers.remove(message.author.id)

    if message.content.lower().startswith(prefixo + 'fazer carinho'):
        adm = message.author.guild.get_role(829909356215926825)
        if user == client.user:
            if adm in message.author.roles:
                embedmessage = discord.Embed(
                    color=colorc, description=(random.choice(repliesaff)))
                embedmessage.set_image(url=random.choice(menheraaffection))
                await message.channel.send(embed=embedmessage)

            else:
                embedmessage = discord.Embed(
                    color=colord, description=(random.choice(repliesrej)))
                embedmessage.set_image(url=random.choice(menherarejection))
                await message.channel.send(embed=embedmessage)

    if message.content.startswith(prefixo + 'rejeitar carinho'):
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colord)
            embedmessage.set_author(
                name=message.author.name + random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)
        else:
            user = message.mentions[0]
            embedmessage = discord.Embed(color=colorb, description=(
                ' rejeitou o carinho de ' + user.mention))
            embedmessage.set_image(url=random.choice(gifsrejection))
            await message.channel.send(embed=embedmessage)

            cooldownmembers.append(message.author.id)
            await asyncio.sleep(10)
            cooldownmembers.remove(message.author.id)

    if message.content.startswith(prefixo + 'morder'):
        if (message.author.id in cooldownmembers):
            embedmessage = discord.Embed(color=colord)
            embedmessage.set_author(
                name=message.author.name + random.choice(replies), icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedmessage)
        else:
            user = message.mentions[0]
            embedMessage = discord.Embed(color=colorb, description=(
                message.author.mention + ' mordeu ' + user.mention))
            embedMessage.set_image(url=random.choice(gifsbite))
            await message.channel.send(embed=embedMessage)

            cooldownmembers.append(message.author.id)
            await asyncio.sleep(5)
            cooldownmembers.remove(message.author.id)

    if message.content.lower() == prefixo + 'cargo':
        embedMessage = discord.Embed(color=colorg, description=(
            message.author.name + ' agora você é veloz e furioso'))
        role = message.author.guild.get_role(  ) # role here
        await message.author.add_roles(role)
        embedMessage.set_image(
            url='https://media.discordapp.net/attachments/660977416176533548/743276560022503564/1504828085_WpRpnj.gif')
        await message.channel.send(embed=embedMessage)


@ client.event
async def on_member_join(member):
    embedmessage = discord.Embed(color=colorp, description=(
        member.mention + random.choice(welcomer)))
    embedmessage.set_thumbnail(url=member.avatar_url)
    welcome = client.get_channel(  ) # channel here
    await welcome.send(embed=embedmessage)


@ client.event
async def on_member_remove(member):
    embedmessage = discord.Embed(
        color=colorp, description=(member.mention + random.choice(goodbyer)))
    embedmessage.set_thumbnail(url=member.avatar_url)
    goodbye = client.get_channel(  ) # channel here
    await goodbye.send(embed=embedmessage)


client.run('  ') # bot's token here
