import Levenshtein
import numpy as np

def exact_match_accuracy(predicted_texts, ground_truth_texts):
    """
    Calculate exact match accuracy between the predicted and ground truth texts.
    
    Args:
        predicted_texts (list): List of predicted corrected texts
        ground_truth_texts (list): List of ground truth correct texts
    
    Returns:
        float: The exact match accuracy (0-1)
    """
    if len(predicted_texts) != len(ground_truth_texts):
        raise ValueError("Predicted and ground truth text lists must have the same length")
    
    correct_count = sum(1 for p, g in zip(predicted_texts, ground_truth_texts) if p == g)
    return correct_count / len(predicted_texts) if len(predicted_texts) > 0 else 0

def character_level_accuracy(predicted_texts, ground_truth_texts):
    """
    Calculate character-level accuracy using Levenshtein distance.
    
    Args:
        predicted_texts (list): List of predicted corrected texts
        ground_truth_texts (list): List of ground truth correct texts
    
    Returns:
        float: The average character-level accuracy (0-1)
    """
    if len(predicted_texts) != len(ground_truth_texts):
        raise ValueError("Predicted and ground truth text lists must have the same length")
    
    accuracies = []
    for pred, gt in zip(predicted_texts, ground_truth_texts):
        distance = Levenshtein.distance(pred, gt)
        max_length = max(len(pred), len(gt))
        accuracy = 1 - (distance / max_length) if max_length > 0 else 1
        accuracies.append(accuracy)
    
    return np.mean(accuracies) if accuracies else 0

def word_level_accuracy(predicted_texts, ground_truth_texts):
    """
    Calculate word-level accuracy.
    
    Args:
        predicted_texts (list): List of predicted corrected texts
        ground_truth_texts (list): List of ground truth correct texts
    
    Returns:
        float: The average word-level accuracy (0-1)
    """
    if len(predicted_texts) != len(ground_truth_texts):
        raise ValueError("Predicted and ground truth text lists must have the same length")
    
    accuracies = []
    for pred, gt in zip(predicted_texts, ground_truth_texts):
        pred_words = pred.split()
        gt_words = gt.split()
        
        # Count correct words
        correct_words = sum(1 for p, g in zip(pred_words, gt_words) if p == g)
        
        # Calculate accuracy
        total_words = max(len(pred_words), len(gt_words))
        accuracy = correct_words / total_words if total_words > 0 else 1
        accuracies.append(accuracy)
    
    return np.mean(accuracies) if accuracies else 0
