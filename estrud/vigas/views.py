from django.contrib import messages
from django.shortcuts import render
from .forms import VigaForm
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Label


def starter(request):
    plot = figure()
    plot.circle([1, 10, 35,  27], [0, 0, 0, 0], size=20, color="blue")
    script, div = components(plot)
    return render(request, 'vigas/starter.html', {'script': script, 'div': div})


def home(request):
    b = 20
    h = 40
    dominio = ''
    lim23 = ''
    lim34 = ''
    x = 20.83
    area_aco = ''
    rcd = 506
    rsd = 506
    md = ''
    esforco = ''
    gama_f = ''
    fcd = ''
    fyd = ''
    fyd2 = ''
    ec2 = ''
    ecd = 3.5
    esd = 5
    mdd = 0
    d = 20
    z = 27.6
    concreto = 0
    fcd2 = 4
    lambida = 0.8
    alpha = 0.85
    memorial = False

    if request.method == 'POST':
        form = VigaForm(request.POST)
        if form.is_valid():
            b = float(form.cleaned_data["b"])
            h = float(form.cleaned_data["h"])
            d = float(form.cleaned_data["d"])
            limite = form.cleaned_data["limites"]
            concreto = float(form.cleaned_data["concreto"])
            aco = float(form.cleaned_data["aco"])
            esforco = float(form.cleaned_data["esforco"])
            gama_f = float(form.cleaned_data["gama_f"])
            fcd = round(concreto/1.4, 2)
            md = esforco * gama_f
            fyd = round(aco/1.15, 2)
            fcd2 = round(fcd*0.1, 2)
            fyd2 = round(fyd*0.1, 2)
            if limite == 'x34':
                if concreto < 50:
                    alpha = 0.85
                    lambida = 0.8
                    ec2 = 2
                    ecd = 3.5
                    mdd = md*100
                    denominador = 0.425*b*(d**2)*fcd*0.1
                    raiz = np.sqrt(1 - (mdd/denominador))
                    x = round(1.25 * d * (1 - raiz), 2)
                    lim23 = round(0.259*d, 2)
                    lim34 = round(0.628*d, 2)
                    area_aco = round(md*100 / ((fyd*0.1)*(d - (0.4) * x)), 2)
                    rcd = round(0.68 * b * x * fcd * 0.1, 2)
                    rsd = round(fyd * 0.1 * area_aco, 2)
                else:
                    alpha = round((0.85*(1-(concreto-50)/200)), 3)
                    lambida = round(0.8 - ((concreto-50)/400), 3)
                    mdd = 2*md*100
                    denominador = alpha*b*(d**2)*fcd*0.1
                    raiz = np.sqrt(1 - (mdd/denominador))
                    x = round(d/lambida * (1 - raiz), 2)
                    ec2 = 2 + 0.085 * (concreto-50)**0.53
                    ecd = round(2.6 + 35 * ((90-concreto)/100)**4, 2)
                    lim23 = round((ecd/(ecd+10))*d, 2)
                    lim34 = round((ecd/(ecd+2.07))*d, 2)
                    rcd = round(alpha * fcd * 0.1 * lambida * x * b, 2)
                    area_aco = round(md*100 / ((fyd*0.1)*(d - (lambida/2) * x)), 2)
                    rsd = round(fyd * 0.1 * area_aco, 2)
                z = round(md*100/rcd, 2)
                esd = round((d-x)*ecd / x, 2)
                if x > lim23 and x < lim34:
                    dominio = 3
            memorial = True
            messages.success(request, 'Seção dimensionada! ')
    else:
        form = VigaForm()

    # Implementação do bokeh
    plot = figure(sizing_mode="scale_both", tools="save, zoom_in, zoom_out")

    plot.toolbar.logo = None

    # Variáveis de eixos auxiliares de desenho
    eixox1 = b/2
    eixox2 = eixox1*5
    eixoy2 = 2 * h
    eixoxcota1 = -4
    eixoxcota3 = 2*eixox1 + 4
    eixoxcota6 = eixox2 + b/2 + 4
    eixoxcota4 = eixox2 - b/2 - 5
    eixoycota2 = eixoy2 - h/2 - 6
    eixoxcota1text = eixoxcota1 - 1
    eixoycota2text = eixoycota2 - 2
    eixoxcota4text = eixoxcota4 - 6
    ponto1cota1 = eixoy2 - h/2
    ponto2cota1 = eixoy2 + h/2
    ponto1cota2 = eixox1 - b/2
    ponto2cota2 = eixox1 + b/2
    ponto1cota3 = eixoy2 - h/2
    ponto2cota3 = eixoy2 + h/2
    ponto1cota4 = eixox2 - b/2
    ponto2cota4 = eixox2 + b/2
    altura_ln = ponto2cota3 - x
    linha_ln = h - x
    eixoycota6text = ponto2cota3 - x/2 - 2
    eixoy2tesao = ponto2cota3 - x/2 + x*0.1
    eixoy1tesao = h - x/2 + x*0.1
    pontoecu_x = eixox1 - ecd

    # Linhas de marcação auxiliares
    plot.line([0, (eixox2 + b/2 + 10)], [0, 0], line_width=1, color="darkgray")

    # Cotas
    # Cota 1
    plot.line([eixoxcota1, eixoxcota1], [ponto1cota1, ponto2cota1], line_width=1, color="dimgray")
    plot.line([(eixoxcota1-2), (eixoxcota1+2)], [ponto1cota1, ponto1cota1], line_width=1, color="dimgray")
    plot.line([(eixoxcota1-2), (eixoxcota1+2)], [ponto2cota1, ponto2cota1], line_width=1, color="dimgray")
    textcota1 = Label(x=eixoxcota1text, y=eixoy2, text='h', background_fill_color="white")
    plot.add_layout(textcota1)

    # Cota 2
    plot.line([ponto1cota2, ponto2cota2], [eixoycota2, eixoycota2], line_width=1, color="dimgray")
    plot.line([ponto1cota2, ponto1cota2], [(eixoycota2-4), (eixoycota2+4)], line_width=1, color="dimgray")
    plot.line([ponto2cota2, ponto2cota2], [(eixoycota2+4), (eixoycota2-4)], line_width=1, color="dimgray")
    textcota2 = Label(x=eixox1, y=eixoycota2text, text='b', background_fill_color="white")
    plot.add_layout(textcota2)

    # Cota 3
    plot.line([eixoxcota3, eixoxcota3], [ponto1cota3, ponto2cota3], line_width=1, color="dimgray")
    plot.line([(eixoxcota3-3), (eixoxcota3+3)], [(eixoy2-h/2*0.8), (eixoy2-h/2*0.8)], line_width=1, color="dimgray")
    plot.line([(eixoxcota3-3), (eixoxcota3+3)], [ponto2cota1, ponto2cota1], line_width=1, color="dimgray")
    plot.line([(eixoxcota3-3), (eixoxcota3+3)], [ponto1cota1, ponto1cota1], line_width=1, color="dimgray")
    textcota3 = Label(x=eixoxcota3+1, y=eixoy2, text='d')
    plot.add_layout(textcota3)
    text2cota3 = Label(x=eixoxcota3+1, y=(eixoy2-h/2), text="d'")
    plot.add_layout(text2cota3)

    # Cota 4
    plot.line([eixoxcota4, eixoxcota4], [ponto1cota1, ponto2cota1], line_width=1, color="steelblue")
    plot.line([(eixoxcota4-2), (eixoxcota4+2)], [ponto1cota1, ponto1cota1], line_width=2, color="steelblue")
    plot.line([(eixoxcota4-2), (eixoxcota4+2)], [ponto2cota1, ponto2cota1], line_width=2, color="steelblue")
    textcota4 = Label(x=eixoxcota4text, y=eixoy2, text=str(h), text_color="steelblue")
    plot.add_layout(textcota4)

    # Cota 5
    plot.line([ponto1cota4, ponto2cota4], [eixoycota2, eixoycota2], line_width=1, color="steelblue")
    plot.line([ponto1cota4, ponto1cota4], [(eixoycota2-4), (eixoycota2+4)], line_width=1, color="steelblue")
    plot.line([ponto2cota4, ponto2cota4], [(eixoycota2+4), (eixoycota2-4)], line_width=1, color="steelblue")
    textcota5 = Label(x=(eixox2-2), y=eixoycota2text, text=str(b), text_color="steelblue", background_fill_color="white")
    plot.add_layout(textcota5)

    # Cota 6
    plot.line([eixoxcota6, eixoxcota6], [altura_ln, ponto2cota3], line_width=1, color="seagreen")
    plot.line([(eixoxcota6-3), (eixoxcota6+3)], [altura_ln, altura_ln], line_width=1, color="seagreen")
    plot.line([(eixoxcota6-3), (eixoxcota6+3)], [ponto2cota3, ponto2cota3], line_width=1, color="seagreen")
    text2cota6 = Label(x=(eixoxcota6), y=eixoycota6text, text=str(x),  text_color="seagreen")
    plot.add_layout(text2cota6)

    # Seta Momento
    plot.circle(eixox1, eixoy2, size=4, color="black")
    plot.line([eixox1, (eixox1*0.2)], [eixoy2, eixoy2], line_width=1, color="black")
    plot.triangle(eixox1*0.2, eixoy2, size=7, angle=1.57, color="black")
    plot.triangle(eixox1*0.3, eixoy2, size=7, angle=1.57, color="black")
    textmk = Label(x=(eixox1*0.5), y=eixoy2, text='Mk')
    plot.add_layout(textmk)

    # As
    plot.rect(x=eixox1, y=eixoy2-h/2*0.8, width=b*0.8, height=2, alpha=0.3, color="black")
    textas = Label(x=eixox1-2, y=eixoy2-h/2*0.75, text='As')
    plot.add_layout(textas)

    # Seção 1
    plot.rect(x=eixox1, y=eixoy2, width=b, height=h, alpha=0.3, color="black")

    # Seção 2
    plot.rect(x=eixox2, y=eixoy2, width=b, height=h, alpha=0.3, color="black")
    plot.rect(x=eixox2, y=eixoy2tesao, width=b, height=(0.8*x), alpha=0.6, color="seagreen")

    # Deformação
    plot.line([eixox1, eixox1], [0, h], line_width=1, color="black")
    plot.line([pontoecu_x, eixox1+esd], [h, 0], line_width=1, color="red")
    textecd = Label(x=pontoecu_x-4, y=h, text=str(ecd),  text_color="red")
    plot.add_layout(textecd)
    textesd = Label(x=eixox1+esd, y=0, text=str(esd),  text_color="red")
    plot.add_layout(textesd)
    plot.circle(pontoecu_x, h, size=4, color="red")
    plot.circle(eixox1+esd, 0, size=4, color="red")

    # Tensões
    plot.line([eixox2, eixox2], [0, h], line_width=3, color="black")
    plot.rect(x=eixox2 + (b*0.3/2), y=eixoy1tesao, width=(b*0.3), height=(0.8*x), alpha=0.6, color="seagreen")
    # Tensoes Rcd
    plot.line([eixox2, (eixox2 + b/2 + 10)], [eixoy1tesao, eixoy1tesao], line_width=2, color="seagreen")
    plot.triangle(eixox2 + 2, eixoy1tesao, size=12, angle=1.57, color="seagreen")
    textrcd = Label(x=(eixox2 + b/2), y=eixoy1tesao, text=str(rcd),  text_color="seagreen")
    plot.add_layout(textrcd)
    # Tensoes Rsd
    plot.line([eixox2, (eixox2 + b/2 + 10)], [(eixoy1tesao-z), (eixoy1tesao-z)], line_width=2, color="royalblue")
    plot.triangle((eixox2 + b/2 + 10), (eixoy1tesao-z), size=12, angle=-1.57, color="royalblue")
    textrsd = Label(x=(eixox2 + b/2), y=eixoy1tesao-z, text=str(rsd),  text_color="royalblue")
    plot.add_layout(textrsd)
    # Linha Neutra
    plot.line([0, (eixox2 + b/2 + 10)], [linha_ln, linha_ln], line_width=1, color="seagreen", line_dash="dashed", line_dash_offset=10)
    textlinhaln = Label(x=-4, y=linha_ln, text=str(x),  text_color="seagreen")
    plot.add_layout(textlinhaln)
    # Renderização do Plot
    script, canvas = components(plot)
    # Variáveis do Template
    context = {
        "form": form,
        "md": md,
        "z": z,
        "esforco": esforco,
        "concreto": concreto,
        "fcd2": fcd2,
        "fyd2": fyd2,
        "d": d,
        "b": b,
        "lambida": lambida,
        "alpha": alpha,
        "gama_f": gama_f,
        "fcd": fcd,
        "fyd": fyd,
        "dominio": dominio,
        "lim23": lim23,
        "lim34": lim34,
        "ec2": ec2,
        "ecd": ecd,
        "esd": esd,
        "x": x,
        "area_aco": area_aco,
        "rcd": rcd,
        "rsd": rsd,
        "memorial": memorial,
        'script': script,
        'canvas': canvas,
    }
    return render(request, 'vigas/home.html', context)
