#!/usr/bin/env bash
set -euo pipefail

# Gera o encerramento comercial vertical do Metodo 3R sem depender de IA para
# desenhar letras. O logo vem da landing page; todo texto e composto pelo
# ffmpeg para permanecer perfeitamente legivel.

LOGO="${1:?uso: gerar-cta-metodo3r.sh <logo.png> <saida.mp4>}"
SAIDA="${2:?uso: gerar-cta-metodo3r.sh <logo.png> <saida.mp4>}"
FONTE_REGULAR="${FONTE_REGULAR:-/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf}"
FONTE_BOLD="${FONTE_BOLD:-/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf}"

test -s "$LOGO" || { echo "logo ausente: $LOGO" >&2; exit 2; }
test -s "$FONTE_REGULAR" || { echo "fonte ausente: $FONTE_REGULAR" >&2; exit 2; }
test -s "$FONTE_BOLD" || { echo "fonte ausente: $FONTE_BOLD" >&2; exit 2; }

QUADRO="$(mktemp --suffix=.png)"
trap 'rm -f "$QUADRO"' EXIT

# Primeiro fechamos a composicao num unico quadro. Alem de tornar o resultado
# reproduzivel, isso impede que diferencas de timebase da imagem do logo mudem
# escala ou enquadramento no meio do MP4.
ffmpeg -y -hide_banner -loglevel error \
  -f lavfi -i "color=c=#FFFFFF:s=1080x1920:r=1:d=1" \
  -i "$LOGO" \
  -filter_complex "
    [1:v]scale=700:-1,format=rgba[logo];
    [0:v]
      drawbox=x=90:y=1040:w=900:h=2:color=#78C9C8@0.55:t=fill,
      drawtext=fontfile=${FONTE_BOLD}:text='AVALIAÇÃO RESPIRATÓRIA':
        fontcolor=#315D83:fontsize=48:x=(w-text_w)/2:y=1105,
      drawtext=fontfile=${FONTE_BOLD}:text='INDIVIDUAL ON-LINE':
        fontcolor=#315D83:fontsize=48:x=(w-text_w)/2:y=1170,
      drawtext=fontfile=${FONTE_REGULAR}:text='com Cássia Saito':
        fontcolor=#4A6A76:fontsize=38:x=(w-text_w)/2:y=1255,
      drawbox=x=145:y=1395:w=790:h=170:color=#2D8A69:t=fill,
      drawtext=fontfile=${FONTE_BOLD}:text='CONVERSE COM CÁSSIA':
        fontcolor=white:fontsize=45:x=(w-text_w)/2:y=1425,
      drawtext=fontfile=${FONTE_REGULAR}:text='PELO WHATSAPP':
        fontcolor=white:fontsize=33:x=(w-text_w)/2:y=1490,
      drawtext=fontfile=${FONTE_REGULAR}:text='Atendimento presencial e on-line':
        fontcolor=#5D7779:fontsize=28:x=(w-text_w)/2:y=1625[base];
    [base][logo]overlay=x=(W-w)/2:y=220:shortest=1,format=rgb24[out]
  " \
  -map "[out]" -frames:v 1 "$QUADRO"

ffmpeg -y -hide_banner -loglevel error \
  -loop 1 -framerate 30 -i "$QUADRO" \
  -vf "fade=t=in:st=0:d=0.45,fade=t=out:st=4.55:d=0.45,format=yuv420p" \
  -an -t 5 -c:v libx264 -preset medium -crf 18 -movflags +faststart "$SAIDA"

echo "$SAIDA"
