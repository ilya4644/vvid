import math


def results(form):
    res_form = dict()
    res_form['res_forearm'] = abs(float(form['forearm']) * float(form['force']) * math.cos(float(form['forearm_angle'])))
    res_form['res_shoulder'] = abs(float(form['shoulder']) * float(form['force']) * math.cos(float(form['shoulder_angle'])))
    res_form['res_back'] = abs(float(form['back']) * float(form['force']) * math.cos(float(form['back_angle'])))
    res_form['res_hip'] = abs(float(form['hip']) * float(form['force']) * math.cos(float(form['hip_angle'])))
    res_form['res_shin'] = abs(float(form['shin']) * float(form['force']) * math.cos(float(form['shin_angle'])))
    res_form['res_foot'] = abs(float(form['foot']) * float(form['force']) * math.cos(float(form['foot_angle'])))
    return res_form
