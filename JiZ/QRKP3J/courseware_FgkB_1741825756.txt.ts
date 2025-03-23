export interface Todo {
    id: number;
    state: TodoState;
}

export enum TodoState {
    Active = 1,
    Complete = 2
}