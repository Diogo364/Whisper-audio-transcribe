import os.path as osp
from argparse import ArgumentParser
import whisper

def set_arguments():
    ap = ArgumentParser()
    ap.add_argument('-f', '--file', type=str, required=True, help='Path to input file')
    ap.add_argument('-o', '--outpath', type=str, default='.', help='Path to transcript output folder')
    ap.add_argument('-m', '--model', type=str, default='base', help='Model type')
    ap.add_argument('--language', type=str, default='pt', help='Input file audio language')
    return vars(ap.parse_args())


if __name__ == '__main__':
    args = set_arguments()
    
    input_basename = osp.basename(args['file'])
    output_file = osp.join(args['outpath'], f'{input_basename}.txt')
    
    model = whisper.load_model(args['model'])
    option = whisper.DecodingOptions(language=args['language'], fp16=False)
    result = model.transcribe(args['file'])
    
    with open(output_file, 'w') as f:
        f.write(result['text'])
