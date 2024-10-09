import pygame
import time


def _load_audio(audio_filename):
    pygame.mixer.music.load(audio_filename)

def play_audio(audio_filename, start_audio = 0):
    _load_audio(audio_filename)
    start_time = time.time()
    pygame.mixer.music.play(start = start_audio)
    return start_time, start_audio

def stop_audio():
    pygame.mixer.music.stop()

def annotate_dict():
    d = {'e': 'verhoorder1', 't': 'verhoorder2', 'a': 'advocaat',
        'o': 'ondervraagde', 'm': 'man onbekende spreker', 
        'v': 'vrouw onbekende spreker', 's':'stilte', 'n': 'noise',
        'E': 'verhoorder1 speaker noise', 'T': 'verhoorder2 speaker noise',
        'A': 'advocaat speaker noise', 'O': 'ondervraagde speaker noise',
        'M': 'man onbekende spreker speaker noise', 
        'V': 'vrouw onbekende spreker speaker noise'}
    return d

def pygame_dict():
    d = {pygame.K_e: 'verhoorder1', pygame.K_t: 'verhoorder2',
        pygame.K_a: 'advocaat', pygame.K_o: 'ondervraagde',
        pygame.K_m: 'man onbekende spreker', 
        pygame.K_v: 'vrouw onbekende spreker',
        pygame.K_s: 'stilte', pygame.K_n: 'noise'}
    return d

def annotation_line(annotation, annot_time, elapsed_time, start_audio,
    audio_filename, annotator_name = ''):
    d = {'annotation': annotation, 'annot_time': annot_time,
        'elapsed_time': elapsed_time, 'start_audio': start_audio,
        'audio_filename': audio_filename, 'annotator_name': annotator_name}
    return d

def annotate_audio(audio_filename, start_audio = 0, end_audio = None,
        annotator_name = 'martijn'):
    pygame.init()
    pygame.mixer.init()
    running = True
    d = annotate_dict()
    pd = pygame_dict()
    start, start_audio = play_audio(audio_filename, start_audio)
    print('started audio')
    if end_audio is not None:
        end_elapsed = start + end_audio - start_audio
    else: end_elapsed = None
    pygame.display.set_mode((1, 1))
    output = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in pd.keys():
                    time_elapsed = time.time()-start
                    annot_time = time_elapsed + start_audio
                    annotation = pd[event.key]
                    print(annotation, time_elapsed, annot_time)
                    line = annotation_line(annotation, annot_time, time_elapsed,
                        start_audio, audio_filename, annotator_name)
                    output.append(line)
                if event.key == pygame.K_q:
                    running = False
        if not pygame.mixer.music.get_busy():
            running = False
        if end_elapsed is not None:
            if time.time() > end_elapsed:
                running = False
        time.sleep(0.05)
    pygame.quit()
    return output
    

