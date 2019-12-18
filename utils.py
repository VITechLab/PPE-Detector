import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


colors = [
    # Bare Head
    [0.716, 0.170, 0.427],

    # Helmet
    [0.388, 0.631, 0.111],

    # Welding Mask
    [0.098, 0.680, 0.468],

    # Ear Protection
    [0.163, 0.075, 0.997],

    # NO Visibility Vest
    [0.849, 0.471, 0.491],

    # High Visibility Vest
    [0.595, 0.554, 0.006],

    # Person
    [0.699, 0.193, 0.917]
]


classes = ['Bare Head', 'Helmet', 'Welding Mask', 'Ear Protection',
           'NO Visibility Vest', 'High Visibility Vest', 'Person']


def visualize_detection(img_file, dets, save_path=None):
        img=mpimg.imread(img_file)
        plt.imshow(img)
        height = img.shape[0]
        width = img.shape[1]
        
        for det in dets:
            x0, y0, x1, y1, score, _, klass = det
            
            cls_id = int(klass)
            xmin = x0
            ymin = y0
            xmax = x1
            ymax = y1
            rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                                 ymax - ymin, fill=False,
                                 edgecolor=colors[cls_id],
                                 linewidth=3.5)
            plt.gca().add_patch(rect)
            class_name = str(cls_id)
            if classes and len(classes) > cls_id:
                class_name = classes[cls_id]
            plt.gca().text(xmin, ymin - 2,
                            '{:s} {:.3f}'.format(class_name, score),
                            bbox=dict(facecolor=colors[cls_id], alpha=0.3),
                                    fontsize=12, color='white')
        plt.axis('off')
        
        if save_path is not None:
            plt.savefig(save_path, bbox_inches='tight')
        
        plt.show()
